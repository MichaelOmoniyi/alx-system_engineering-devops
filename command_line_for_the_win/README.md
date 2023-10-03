
---

# Project Name README

## Uploading Completed Levels Screenshots

This project requires uploading screenshots of the completed levels to a sandbox environment. Follow the steps below to accomplish this task:

### Step 1: Take Screenshots of Completed Levels

Ensure you have taken screenshots of the completed levels as mentioned in the general requirements. Save these screenshots in a specific folder on your local machine.

### Step 2: Establish an SFTP Connection to Sandbox Environment

Open a terminal or command prompt on your local machine.

```bash
sftp username@hostname
```

Replace `username` with your provided username and `hostname` with the provided hostname. Enter your password when prompted.

### Step 3: Navigate to the Destination Directory

Once connected, navigate to the directory where you want to upload the screenshots.

```bash
cd path/to/sandbox/directory
```

### Step 4: Upload Screenshots

Use the `put` command to upload screenshots from your local machine to the sandbox environment.

```bash
put /path/to/local/screenshots/folder/*.png
```

Replace `/path/to/local/screenshots/folder/*.png` with the actual path to your local screenshots folder. The `*` wildcard character is used to upload all `.png` files in the folder.

### Step 5: Confirm Transfer

Confirm that the screenshots have been successfully transferred by checking the sandbox directory.

```bash
ls
```

This command will list the files in the current directory. Ensure your screenshots are visible in the list.

### Step 6: Push Screenshots to GitHub

Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.

---

**Note:** Make sure to replace placeholders such as `username`, `hostname`, `/path/to/local/screenshots/folder/`, and any other specific paths or names with the actual values relevant to your setup.
