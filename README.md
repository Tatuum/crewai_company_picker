# CompanyPicker Crew

A collaborative multi-agent AI system built with [crewAI](https://crewai.com) that analyzes trending companies and picks the best investment opportunities. This project demonstrates how specialized AI agents can work together to deliver comprehensive financial analysis with minimal human input.

## 🚀 Features

- **Trending Company Discovery**: AI agents find the latest trending companies in specified sectors
- **Comprehensive Financial Analysis**: Deep research and analysis of company fundamentals
- **Intelligent Stock Picking**: Advanced algorithms select the best investment opportunities
- **Push Notifications**: Real-time alerts with investment decisions and rationale
- **Detailed Reporting**: Comprehensive reports on selected and rejected companies

## 📋 Prerequisites

- Python >= 3.10, < 3.14
- [UV](https://docs.astral.sh/uv/) package manager
- OpenAI API key

## 🛠️ Installation

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Navigate to the project**:
   ```bash
   cd company_picker
   ```

3. **Install dependencies**:
   ```bash
   crewai install
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎯 Quick Start

Run the CompanyPicker crew with:
```bash
crewai run
```

This will analyze trending companies in the fashion sector and pick the best investment opportunity.

## 📁 Project Structure

```
company_picker/
├── src/company_picker/
│   ├── config/
│   │   ├── agents.yaml      # Agent definitions and configurations
│   │   └── tasks.yaml       # Task definitions and workflows
│   ├── tools/
│   │   └── push_tool.py     # Custom tools for agents
│   ├── crew.py              # Crew orchestration logic
│   └── main.py              # Entry point and sector configuration
├── output/                  # Generated analysis and reports
├── knowledge/               # Knowledge base and context
└── tests/                   # Test files
```

## ⚙️ Configuration

### Agents (`src/company_picker/config/agents.yaml`)

The project uses four specialized agents:

1. **Trending Company Finder** - Discovers trending companies in the news
2. **Financial Researcher** - Provides comprehensive company analysis
3. **Stock Picker** - Selects the best investment opportunity
4. **Manager** - Orchestrates the entire analysis process

### Tasks (`src/company_picker/config/tasks.yaml`)

Tasks define the analysis workflow:
- **Find Trending Companies**: Discover new trending companies in specified sectors
- **Research Companies**: Conduct detailed financial analysis
- **Pick Best Company**: Select optimal investment with push notification

## 🔧 Customization

Edit `src/company_picker/main.py` to change the sector or analysis parameters:

```python
inputs = {
    'sector': 'technology'  # Change sector here
}
```

## 📊 Example Output

The crew generates:
- `output/trending_companies.json` – List of discovered trending companies
- `output/research_report.json` – Detailed financial analysis
- `output/decision.md` – Final investment decision with rationale
