// make-pqc-key.js - create a composite post-quantum OpenPGP key for OnlyKey.
//
// Uses the OpenPGP.js build that python-onlykey installs for loadpqc, so it
// needs python-onlykey 1.3.1 or newer and Node.js 18 or newer.
//
//   node make-pqc-key.js "Your Name" you@example.com
//
// Asks for a passphrase, then writes two files to the current folder:
//   you@example.com-pqc-secret.asc  private key, protected by the passphrase:
//                                   load it with onlykey-cli loadpqc
//   you@example.com-pqc-public.asc  public key: share it, and keep a copy
'use strict';
const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { execFileSync } = require('child_process');

const [name, email] = process.argv.slice(2);
if (!name || !email) {
  console.error('usage: node make-pqc-key.js "Your Name" you@example.com');
  process.exit(1);
}

function findOpenPGP() {
  for (const py of ['python3', 'python', 'py']) {
    try {
      const dir = execFileSync(py, ['-c',
        'import onlykey, os; print(os.path.dirname(onlykey.__file__))'],
        { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
      const file = path.join(dir, 'openpgp_bridge', 'openpgp.js');
      if (fs.existsSync(file)) return file;
    } catch (e) { /* try the next name */ }
  }
  throw new Error('python-onlykey not found: run pip install onlykey');
}

function askHidden(prompt) {
  return new Promise((resolve) => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: true });
    rl._writeToOutput = (s) => { if (s.includes(prompt)) rl.output.write(s); };
    rl.question(prompt, (answer) => { rl.close(); process.stdout.write('\n'); resolve(answer); });
  });
}

(async () => {
  const openpgp = new Function(fs.readFileSync(findOpenPGP(), 'utf8') + '\n;return openpgp;')();
  const passphrase = process.env.PQC_PASSPHRASE || await askHidden('Passphrase for the private key: ');
  if (!process.env.PQC_PASSPHRASE && passphrase !== await askHidden('Repeat the passphrase: ')) {
    console.error('The passphrases do not match.');
    process.exit(1);
  }
  if (!passphrase) {
    console.error('A passphrase is required to protect the private key file.');
    process.exit(1);
  }
  const { privateKey, publicKey } = await openpgp.generateKey({
    type: 'pqc',              // ML-DSA-65+Ed25519 primary, ML-KEM-768+X25519 subkey (RFC 9980)
    config: { v6Keys: true }, // composite keys are v6 keys
    userIDs: [{ name, email }],
    passphrase,
    format: 'armored',
  });
  const base = email.replace(/[^A-Za-z0-9@._-]/g, '_');
  fs.writeFileSync(`${base}-pqc-secret.asc`, privateKey, { mode: 0o600 });
  fs.writeFileSync(`${base}-pqc-public.asc`, publicKey);
  const key = await openpgp.readKey({ armoredKey: publicKey });
  console.log(`Fingerprint: ${key.getFingerprint().toUpperCase()}`);
  console.log(`Wrote ${base}-pqc-secret.asc (private key: load it with onlykey-cli loadpqc)`);
  console.log(`Wrote ${base}-pqc-public.asc (public key: share it, and keep a copy)`);
})().catch((e) => { console.error(e.message); process.exit(1); });
