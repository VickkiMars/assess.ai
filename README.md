# assess.ai

## Overview
The **assess.ai AI-Powered Script Marker** is an intelligent grading system designed to evaluate and score scripts, assignments, or tests automatically. Leveraging state-of-the-art Natural Language Processing (NLP) techniques, it provides accurate, consistent, and unbiased evaluations, significantly reducing grading time and enhancing scalability for educational institutions and professional settings.

---

## Features

- **Automated Scoring:** Evaluates written responses against predefined rubrics or criteria.
- **Natural Language Understanding:** Handles diverse writing styles and interprets semantic meaning effectively.
- **Customizable Rubrics:** Supports configurable scoring rules to adapt to different use cases.
- **Feedback Generation:** Provides detailed feedback on each response, highlighting strengths and areas for improvement.
- **Batch Processing:** Capable of grading multiple scripts simultaneously, increasing efficiency.
- **Scalability:** Handles small-scale classroom grading to large-scale institutional requirements.

---

## Use Cases

- **Education:** Automate grading for essays, assignments, and exams.
- **Corporate Training:** Assess employee performance in training programs.
- **Certification Programs:** Grade scripts in online or offline certification exams.
- **Recruitment:** Evaluate written responses in candidate assessments.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-script-marker.git
   cd ai-script-marker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage

### 1. Configure Rubrics
Define the grading criteria in the `rubrics.json` file. Example:
```json
{
    "clarity": 40,
    "originality": 30,
    "grammar": 20,
    "relevance": 10
}
```

### 2. Input Scripts
Place the scripts to be graded in the `input_scripts` directory as `.txt` files.

### 3. Execute Grading
Run the following command to process scripts:
```bash
python grade.py
```

### 4. View Results
Graded results and feedback will be saved in the `output_results` directory as `.csv` files.

---

## Configuration

### Environment Variables
Set the following environment variables for advanced configurations:
- `MODEL_PATH`: Path to the pre-trained AI model (default: `models/default_model.pt`).
- `LOG_LEVEL`: Logging level (default: `INFO`).

### Advanced Options
Modify the `config.yaml` file to customize additional settings, such as:
- Batch size
- Language preferences
- Feedback verbosity

---

## Architecture

The AI-Powered Script Marker comprises the following modules:

1. **Input Processor:** Prepares scripts for analysis by tokenizing and cleaning input.
2. **Scoring Engine:** Applies NLP models to evaluate scripts against rubrics.
3. **Feedback Generator:** Generates actionable insights and suggestions.
4. **Output Writer:** Saves scores and feedback in user-friendly formats.

---

## Contributing

We welcome contributions to improve this project. Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

For questions, issues, or feature requests, please contact us at [support@assess.ai](mailto:victorumoreng@gmail.com) or create an issue in the GitHub repository.

---

## Acknowledgments
******
