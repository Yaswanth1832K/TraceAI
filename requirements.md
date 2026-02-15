This document was initially generated using Kiro and then reviewed and refined by our team to match the implemented prototype.

Project Name: TraceAI
Team Members: Yaswanth Jallipalli,Kanishkhan,Prakyath Nandigam,Nikshith Gurram

1. Introduction

TraceAI is an AI-powered debugging assistant designed to help students and beginner developers understand and fix errors in unfamiliar codebases.

Instead of searching forums or repeatedly trying random fixes, users can upload a project repository and paste an error message. The system analyzes relevant project files and explains the likely cause of the error along with suggested solutions.

The goal of TraceAI is not to replace developers, but to support learning and faster onboarding into real-world software projects.

2. Problem Statement

Debugging is one of the most time-consuming activities in software development, especially for new developers. Many errors occur due to configuration issues, dependency problems, or misunderstanding of program flow.

Existing resources such as documentation, forums, and chatbots provide generic answers because they cannot access the actual project. As a result, developers spend hours locating the real cause of a simple problem.

TraceAI addresses this gap by analyzing the user’s real codebase together with runtime error logs.

3. Target Users

Computer science students

Internship developers

Open-source contributors

Developers onboarding into new projects

4. Functional Requirements
4.1 Project Upload

The system accepts a GitHub repository link or ZIP file.

The system extracts source files from the project.

The system confirms successful upload to the user.

4.2 Error Input

Users can paste runtime errors or crash logs.

The system identifies key details such as error type and stack trace.

The system notifies the user if the error text is unclear.

4.3 Project Indexing

The system scans project files and prepares them for search.

Important code sections (imports, functions, classes) are identified.

The user is notified when indexing is complete.

4.4 Context Retrieval

The system finds files relevant to the error.

The system extracts surrounding code context.

Relevant files are ranked by relevance.

4.5 Root Cause Analysis

The system uses an AI model to analyze the error and related code.

The system explains the likely cause in simple language.

The system points to relevant files and code locations.

4.6 Fix Recommendation

The system suggests possible fixes.

Suggestions may include commands or code edits.

The system explains why the fix should resolve the issue.

4.7 Result Presentation

The output contains:

Root cause explanation

Related code snippet

Suggested solution

Users can copy the recommended fix.

5. Non-Functional Requirements

The interface should be simple and beginner-friendly.

The system should respond within a reasonable time for small projects.

Explanations should be written in clear English.

The prototype focuses on JavaScript/Node.js projects.

6. Privacy and Security

Uploaded code is used only for analysis.

Files are stored temporarily.

Data is not shared with other users.

7. Limitations

The prototype supports small to medium-sized projects.

The system provides best-effort suggestions and may not always be correct.

TraceAI assists debugging but does not replace developer judgment.

8. User Workflow

A typical usage of TraceAI follows these steps:

The user uploads a GitHub repository or project ZIP file.

The system scans and indexes the project files.

The user pastes a runtime error or crash message.

The system retrieves relevant code sections.

TraceAI analyzes the error together with the code.

The system presents:

explanation of the error

probable root cause

suggested fix

This workflow is designed to mirror a real debugging process while reducing the time required to locate the problem.

9. Responsible AI Considerations

TraceAI provides guidance and assistance but does not automatically modify user code.

Important considerations:

Suggestions may not always be correct.

Developers must review recommendations before applying changes.

The system is intended as a learning and productivity aid.

The system does not access private user credentials or external services.

10. Evaluation Plan

We will evaluate the effectiveness of TraceAI using practical debugging scenarios:

Missing dependency errors

Incorrect import paths

Configuration mistakes

Permission errors

Success Criteria:

The system identifies the correct file involved in the error

The explanation is understandable to a beginner

The suggested fix helps resolve the issue
