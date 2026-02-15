# TraceAI Demo Steps

Follow these steps to demonstrate the power of TraceAI using the provided sample project.

## Prerequisites
- Python 3.9+
- Node.js (for the sample app)
- An LLM API Key (OpenAI/Anthropic)

## Step 1: Initialize the Environment
1. Navigate to the `backend/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Step 2: Setup the Sample Project
1. Navigate to `sample_project/broken-node-app/`.
2. run the app to see it fail:
   ```bash
   node index.js
   ```
3. **Expected Error:** `Error: Cannot find module 'express'`. (Note: Express is imported but not included in `package.json` dependencies).

## Step 3: Run TraceAI Analysis
1. Start the backend:
   ```bash
   python app.py
   ```
2. Upload the `sample_project/broken-node-app/` folder via the interface (or CLI tool).
3. Paste the error log from Step 2 into the analysis box.

## Step 4: Review the Fix
1. TraceAI will analyze `index.js` and `package.json`.
2. **Analysis Result:** TraceAI should identify that `express` is imported in `index.js` but missing from `package.json`.
3. **Suggested Fix:** `npm install express` or adding express to `dependencies`.

## Step 5: Verify the Fix
1. Apply the suggested fix.
2. Run `node index.js` again to confirm the bug is resolved.
