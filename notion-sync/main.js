const { Plugin } = require('obsidian');
const { exec } = require('child_process');
const path = require('path');
// Define your Python script and arguments
// Get the Obsidian vault directory path
const vaultDirectoryPath = this.app.vault.adapter.basePath;

// Define your relative file path within the plugin folder
const relativeFilePath = '.obsidian/plugins/notion-sync/notion1.py';
console.log('Vault Directory Path:', vaultDirectoryPath);
console.log('Relative File Path:', relativeFilePath);
// Create the absolute file path by joining vault directory and relative file path
const pythonScript = path.resolve(vaultDirectoryPath, relativeFilePath);


// Construct the command string with arguments

class NotionSync extends Plugin {
    onload() {
        console.log('Your plugin has been loaded!');

        // Execute Python script when Obsidian starts
        this.executePythonScript(pythonScript);

        // Your plugin logic goes here
    }

    onunload() {
        console.log('Your plugin has been unloaded!');

        // Execute Python script when Obsidian exits
        this.executePythonScript(pythonScript);
    }

    executePythonScript(scriptPath) {
        try {
            // Construct the command to run the Python script
            const command = `python "${pythonScript}"`;

            // Execute the command asynchronously
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    console.error(`Error executing Python script: ${error.message}`);
                    return;
                }
                console.log(`Python script executed successfully. Output: ${stdout}`);
            });
        } catch (error) {
            console.error(`Error executing Python script: ${error.message}`);
        }
    }
}



module.exports = NotionSync;