# Connecting to the Private Ethereum Blockchain

## Overview
This project guides users through connecting to a private Ethereum blockchain, exploring it, and performing a few operations. It's designed for educational purposes to simulate interactions with the Ethereum blockchain without the costs or legal issues associated with the main network.

## Prerequisites
- A recent version of Python 3
- Ability to install Python packages via pip
- Permission to install applications on your machine

## Installation

### Geth Installation
1. Download and install `geth` (Go Ethereum) from the [geth downloads page](https://geth.ethereum.org/downloads/).
2. Follow the installation instructions specific to your operating system.
3. **Warning:** Do not run `geth` without specific command options; it will attempt to download the entire Ethereum blockchain.

## Connecting to the Blockchain

### Step 1: Directory Setup
Create a directory to store blockchain information, referred to as `/path/to/ethprivate` in this guide.

### Step 2: Genesis Block
Copy the provided `genesis.json` file into your data directory. Do not modify this file.

### Step 3: Initialize Geth
Initialize `geth` with the genesis block by running:


### Step 4: Configuration
Modify the provided `geth-config.toml` file with your data directory and UVA userid.

### Step 5: Start Geth
Run `geth` with the modified configuration:


## Geth Interaction

### Attach to Geth Node
To interact with the blockchain, attach to the local Ethereum node using:



### Interacting with Geth
- Check connection with `admin.peers.length`
- Sync status can be checked with `eth.syncing`
- Create a new account with `personal.newAccount()`
- Check account balance with `eth.getBalance(eth.coinbase)`

## Acquiring Ether

Use the course Ethereum Faucet to receive (fake) ETH for your account.

## Key Extraction

Extract your account's private key from the `keystore/` directory for use in dApp development.

## Sending Ether

Send (fake) ETH to the course-wide address as instructed in part 6 of the assignment.

## Exploring Geth

Explore various `geth` modules and functions through the JavaScript console.

## Blockchain Explorer

Use the web-based blockchain explorer to view transactions and blocks related to your account.

## Submission

Submit the completed `ethprivate.py` file, documenting your interactions with the private Ethereum blockchain.

## Closing Remarks

Remember to shut down your `geth` node when not in use to comply with UVA ITS policies.

---

## Contact Information

For any queries or assistance, please contact the course instructor or TAs.
