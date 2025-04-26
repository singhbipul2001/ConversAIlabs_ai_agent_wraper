# AI Agent Creation Wrapper API

This project provides a unified API to create AI agents using either Vapi or Retell AI's agent creation APIs. It standardizes the input parameters to simplify the user experience.

## Overview
The API exposes a single endpoint, `/create-agent`, which accepts POST requests with JSON data. Users specify the provider (`vapi` or `retell`) and provide standardized parameters. The backend translates these into the appropriate format for the chosen provider's API.

## Setup
1. **Prerequisites**:
   - Python 3.8+
   - Flask, requests, and python-dotenv libraries

2. **Installation**:
   ```bash
   pip install -r requirements.txt
