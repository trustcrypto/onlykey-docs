const { defineConfig } = require('@docmd/core');

module.exports = defineConfig({
  title: 'OnlyKey Docs',
  description: 'Documentation for OnlyKey hardware security tokens by CryptoTrust.',
  url: 'https://docs.onlykey.io',

  // Sidebar order mirrors the previous site (docs.onlykey.io).
  // The 404 page is intentionally omitted so it does not appear in the sidebar.
  navigation: [
    {
      title: 'General Information',
      collapsible: true,
      children: [
        { title: 'Get Started', path: '/' },
        { title: 'FAQs', path: '/faq' },
        { title: 'About Security', path: '/security' },
      ],
    },
    { title: "OnlyKey User's Guide", path: '/usersguide' },
    { title: "OnlyKey DUO User's Guide", path: '/duousersguide' },
    { title: 'Features', path: '/features' },
    {
      title: 'Apps and Software',
      collapsible: true,
      children: [
        { title: 'Desktop App', path: '/app' },
        { title: 'WebCrypt (OpenPGP Webapp)', path: '/webcrypt' },
        { title: 'SSH/GPG Agent (onlykey-agent)', path: '/onlykey-agent' },
        { title: 'Command-Line Utility (onlykey-cli)', path: '/command-line' },
        { title: 'Firmware', path: '/firmware' },
      ],
    },
    {
      title: 'Knowledge Base',
      collapsible: true,
      children: [
        { title: 'Works with OnlyKey', path: '/workswithonlykey' },
        { title: 'Upgrade Guide', path: '/upgradeguide' },
        { title: 'Legacy Firmware Upgrade Guide', path: '/legacyupgradeguide' },
        { title: 'International Travel Edition Guide', path: '/ite' },
        { title: 'Plausible Deniability Setup Guide', path: '/pdguide' },
        { title: 'Windows Active Directory Guide', path: '/activedirectory' },
        { title: 'Linux - Using OnlyKey with Linux', path: '/linux' },
        { title: 'Mobile - Using OnlyKey with iOS and Android', path: '/mobile' },
        { title: 'OpenPGP Keys - Import from Protonmail, Keybase, Mailvelope', path: '/importpgp' },
        { title: 'Virtual Machines with OnlyKey', path: '/virtualmachines' },
        { title: 'Qubes OS with OnlyKey', path: '/qubes' },
        { title: 'Full-Disk Encryption with OnlyKey', path: '/full-disk-encryption' },
        { title: 'OpenSSH With OnlyKey', path: '/openssh' },
        { title: 'KeepassXC Upgrade Guide', path: '/keepassxc-upgrade' },
        { title: 'Windows Subsystem for Linux (WSL)', path: '/wsl' },
      ],
    },
  ],
});
