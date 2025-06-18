# AI-Powered Virtual Teaching Assistant

An intelligent chatbot system that provides automated responses to student queries by leveraging course materials and discussion forums. This application demonstrates how AI can enhance educational support through contextual understanding.

## About This Project

I developed this virtual assistant to explore the intersection of natural language processing and educational technology. The system intelligently processes student questions and provides relevant answers by analyzing:

- Educational content from various online sources
- Community discussion threads and Q&A forums
- Course-related documentation and materials

## Key Features

- **Smart Query Processing**: Handles text-based questions with optional image attachments
- **Contextual Responses**: Provides accurate answers by referencing relevant source materials
- **Source Attribution**: Includes links to original content when applicable
- **RESTful API**: Clean, well-documented endpoints for easy integration
- **Cloud Deployment**: Hosted on reliable cloud infrastructure for 24/7 availability

## Technical Stack

- **Backend**: Python with Flask framework for robust API development
- **AI Integration**: OpenAI GPT models for natural language understanding
- **Deployment**: Cloud hosting with automated CI/CD pipeline
- **Data Processing**: Custom scraping and preprocessing algorithms
- **Web Interface**: Interactive documentation and testing interface

## API Usage

The system exposes a RESTful API for seamless integration:

**Endpoint**: `POST /api/`

**Request Format**:
```json
{
  "question": "Your question here",
  "image": "base64_encoded_image_data (optional)"
}
```

**Response Format**:
```json
{
  "answer": "Detailed response to your question",
  "links": [
    {
      "url": "reference_link",
      "text": "link_description"
    }
  ]
}
```

## Live Application

You can interact with the deployed application here: [Virtual TA Demo](https://tds-project1-virtual-ta-hbpl.onrender.com/docs)

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Step-by-Step Setup

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd tds-project1-virtual-ta
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   
   Create a `.env` file in the project root directory:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your OpenAI API key:
   ```
   API_KEY=sk-proj-your_openai_api_key_here
   ```
   
   **Important**: 
   - Your API key should start with `sk-proj-` (for project keys) or `sk-` (for legacy keys)
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Make sure you have sufficient credits in your OpenAI account

4. **Validate your API key setup**
   ```bash
   python validate_api_key.py
   ```
   
   This script will check if your API key is correctly configured and can connect to OpenAI.

5. **Process the knowledge base (first-time setup)**
   ```bash
   python preprocess.py
   ```
   
   This will create embeddings for the knowledge base. If you get authentication errors:
   - Verify your API key is correctly set in the `.env` file
   - Check that your API key hasn't expired
   - Ensure you have available credits in your OpenAI account

6. **Run the application**
   ```bash
   python app.py
   ```

### Troubleshooting

**Authentication Errors (Status 401)**
- Double-check your API key format in the `.env` file
- Ensure the API key starts with `sk-proj-` or `sk-`
- Verify the key hasn't expired on the OpenAI platform
- Check your OpenAI account has sufficient credits

**Rate Limiting (Status 429)**
- The system will automatically retry with exponential backoff
- Consider upgrading your OpenAI plan for higher rate limits

### Environment Variables

- `API_KEY`: Your OpenAI API key (required)

## Data Sources

The system automatically manages its knowledge base, which is updated periodically to ensure relevant and current information.

## License

This project is available under the MIT License - see the [LICENSE](LICENSE) file for more information.

---

*This project showcases the potential of AI-driven educational tools and demonstrates practical applications of natural language processing in academic environments.*
