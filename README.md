# entropy

## Prequisite

  `$ pip install -r requirements.txt`

## Generate High-Entropy GPG key using Diceware

For example, if you are using an Air-Gapped machine which has a too low entropy
to generate a strong key.  You can increase entropy by importing your high
entropy words list.


1. Set up a temporary GPG environment:

  `$ export GNUPGHOME=$(mktemp -d)`
  `$ cd $GNUPGHOME`

2. Generate and import the generated `words.txt`

3. Hash it: `$ echo -n $(cat words.txt) | sha256sum | awk '{print $1}' > hash.txt`

4. Convert into a `/dev/random` digestible binary: `$ xxd -r -p hash.txt > seed.bin`

  `$ sudo sh -c 'cat seed.txt > /dev/random'`

5. Feed the binary data into the entropy pool:

  `$ sudo dd if=seed.bin of=/dev/random bs=512 count=2`

6. Create a `gen-key-script` file with the following content:

```
  %echo Generate master key
  Key-Type: ECC
  Key-Curve: ed25519
  Name-Real: clem
  Name-Comment: come up slow down
  Name-Email: clemedon@icloud.com
  Expire-Date: 0
  %commit

  %echo Add encryption subkey
  Subkey-Type: ECC
  Subkey-Curve: cv25519
  Subkey-Usage: encrypt
  Expire-Date: 0
  %commit

  %echo Add signing subkey
  Subkey-Type: ECC
  Subkey-Curve: ed25519
  Subkey-Usage: sign
  Expire-Date: 0
  %commit

  %echo Add authentication subkey
  Subkey-Type: ECC
  Subkey-Curve: ed25519
  Subkey-Usage: auth
  Expire-Date: 0
  %commit

  %echo done
```

Generate key: `$ gpg --batch --gen-key gen-key-script`
Verify the Generated Keys: `$ gpg --list-secret-keys`
