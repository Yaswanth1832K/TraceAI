# TraceAI – Software Requirements Specification (SRS)

## 1. Introduction
TraceAI is an AI-powered debugging assistant designed to help students and beginner developers understand and fix errors in unfamiliar codebases. By analyzing the user’s real codebase together with runtime error logs, it provides contextualized root-cause analysis and fix suggestions.

## 2. Problem Statement
Debugging is time-consuming, especially for new developers. Errors often stem from configuration issues or misunderstood program flow. Existing resources (Stack Overflow, LLMs) often lack the project-specific context needed to solve niche bugs quickly.

## 3. Target Users
- Computer science students
- Intern developers
- Open-source contributors
- Developers onboarding into new projects

## 4. Functional Requirements
### 4.1 Project Upload
- The system shall accept a project repository (GitHub link or local directory).
- The system shall extract and parse source files.

### 4.2 Error Input
- The system shall provide a text area for users to paste runtime errors or stack traces.
- The system shall identify key error characteristics (type, file, line number).

### 4.3 Indexing & Retrieval
- The system shall generate embeddings for project code sections.
- The system shall store chunks in a local vector database for semantic search.
- The system shall retrieve the top-K relevant code sections based on the input error log.

### 4.4 Analysis & Output
- The system shall use an LLM to analyze the retrieved context and the error.
- The system shall present a root cause explanation.
- The system shall provide a suggested code fix or command.

## 5. Non-Functional Requirements
- **Usability:** The UI should be minimal and intuitive.
- **Speed:** Retrieval and analysis should complete within 10-20 seconds for small projects.
- **Language Support:** Initial focus on JavaScript/Node.js and Python.

## 6. Privacy Considerations
- Code is processed locally or via API; not used for training external models beyond the specific analysis request.
- Temporary storage of project files during the session.

## 7. Limitations
- Optimized for small to medium-sized repositories.
- Logical bugs that require deep execution tracing may be harder to detect than configuration or syntax errors.

## 8. User Workflow
1. User uploads project.
2. System indexes the codebase.
3. User pastes error log.
4. System retrieves relevant code.
5. AI generates diagnosis and fix.
6. User applies the fix.

## 9. Responsible AI Considerations
- Users are reminded that AI suggestions are probabilistic and should be reviewed.
- The system does not automatically execute suggested code or commands.

## 10. Evaluation Plan
Success is measured by the system's ability to correctly identify the file and line responsible for intentional bugs in the `sample_project/`.
