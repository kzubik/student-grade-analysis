# Student Grade Analysis Project

This project analyzes a comprehensive student grading dataset to understand various factors affecting student performance. The analysis includes statistical tests, visualizations, and insights about student grades, study habits, and other relevant factors.

## Features

- Comprehensive data analysis of student performance
- Statistical analysis including correlation studies and t-tests
- Multiple visualizations:
  - Grade distribution
  - Correlation matrix
  - Study hours vs. performance analysis
  - Score distribution by study hours
- Detailed statistical reports

## Dataset

The dataset used in this analysis contains information about 5,000 students, including:
- Academic performance metrics
- Study habits
- Personal information
- Family background
- Stress levels and sleep patterns

Source: [Kaggle - Students Grading Dataset](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset)

## Requirements

- Python 3.8+
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scipy
  - kaggle

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kzubik/student-grade-analysis.git
cd student-grade-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up Kaggle API credentials:
   - Go to your Kaggle account settings
   - Download your API credentials (kaggle.json)
   - Place the file in `~/.kaggle/` directory
   - Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

## Usage

Run the analysis script:
```bash
python student_analysis.py
```

The script will:
1. Download the dataset (if not already present)
2. Perform the analysis
3. Generate visualizations in the `visualizations` directory
4. Create a detailed report in `analysis_results.txt`

## Project Structure

```
student-grade-analysis/
├── README.md
├── requirements.txt
├── student_analysis.py
├── visualizations/
│   ├── grade_distribution.png
│   ├── correlation_matrix.png
│   ├── score_vs_study_hours.png
│   └── score_vs_hours_scatter.png
└── analysis_results.txt
```

## Results

The analysis reveals several interesting insights about student performance:

1. Grade Distribution:
   - A: 29.9%
   - B: 19.6%
   - C: 15.9%
   - D: 17.8%
   - F: 16.8%

2. Study Hours Impact:
   - Weak correlation between study hours and total score (-0.013)
   - No significant difference between high and low study hours groups

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- GitHub: [kzubik](https://github.com/kzubik) 