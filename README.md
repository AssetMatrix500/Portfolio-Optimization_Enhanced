This project enhances Daniel Carpenter's Portfolio Optimization model, particularly focused on maximizing Sharpe ratio for dividend-focused investors. The model uses Particle Swarm Optimization (PSO) to find the optimal portfolio allocation while incorporating several sophisticated adjustments that improve real-world performance.

## Table of Contents
- 1 [Key Enhancements](#key-enhancements)
- 2 [Additional Enhancements](#additional-enhancements)
- 3 [About the PSO Approach to MPT](#about-the-pso-approach-to-mpt)
- 4 [Quick Start](#quick-start)
- 5 [Implementation Note](#implementation-note)
- 6 [Acknowledgment](#acknowledgment)
- 7 [License](#license)
- 8 [Professional Services]
- 9 [Attribution and Contributions](#attribution-and-contributions)
- 10[Disclaimer](#disclaimer)
--------------------------------------------------------------------------------------------------------------------------
1. Key Enhancements
--------------------------------------------------------------------------------------------------------------------------
Core Methodological Improvements

Bayesian Shrinkage for Expected Returns

Reduces estimation error by intelligently "shrinking" extreme return expectations toward more reasonable priors
Uses asset-specific priors based on market cap and industry classification
Significantly improves out-of-sample performance by preventing optimizer oversensitivity to outliers


Blume-Adjusted Betas in Factor Model

Implements regression coefficient adjustments following Blume's methodology
Corrects for the statistical tendency of betas to revert toward 1.0 over time
Creates more stable covariance estimates, particularly important for long-term investments


Portfolio Results Averaging

Runs multiple PSO optimization passes and averages the results
Produces more stable and robust allocation recommendations
Reduces sensitivity to the random nature of PSO's search pattern


--------------------------------------------------------------------------------------------------------------------------
2. Additional Enhancements
--------------------------------------------------------------------------------------------------------------------------

Dividend Reinvestment Plan (DRIP) Support

Simulates the compounding effect of reinvested dividends
Realistic modeling of how dividends affect long-term performance
Particularly valuable for Dividend Kings universe optimization


Flexible Monthly Contributions

Supports user-defined contribution amounts
Models realistic investment behavior with periodic capital injections
Shows compounding effects of consistent investing over time


Rolling Optimization Windows

Uses 36-month rolling windows to adapt to changing market conditions
Avoids overfitting to single market regimes
Provides more reliable performance across different market cycles


Advanced Drawdown Analysis

Calculates and visualizes portfolio drawdowns
Statistical analysis of drawdown severity and duration
Provides z-score metrics to contextualize drawdown events

--------------------------------------------------------------------------------------------------------------------------
3. About the PSO Approach to MPT
--------------------------------------------------------------------------------------------------------------------------
Unlike traditional MPT approaches that use quadratic programming, this model uses Particle Swarm Optimization (PSO) to explore the space of possible portfolios in a non-deterministic way. This has several advantages:

Note on Optimization Approach: While this model can optimize for minimum risk ("risk" parameter), the "Sharpe" parameter was rigorously tested and found to produce superior portfolios at the point of tangency on the efficiency frontier.
Dual Capital Market Lines: The presence of two capital market lines is intentional and not an error. The traditional Capital Market Line (green dashed line) represents theoretical optimal portfolios from classic MPT. The PSO-derived Capital Market Line (magenta dashed line) represents what our adaptive algorithm found through its exploration of the portfolio space.
Adaptive Correction: The PSO approach corrects for unrealistic conclusions often found in deterministic MPT calculations. By exploring the actual portfolio space rather than relying purely on mathematical abstractions, it finds solutions that better reflect real-world constraints and behaviors.

--------------------------------------------------------------------------------------------------------------------------
4. ## Quick Start
--------------------------------------------------------------------------------------------------------------------------

IMPORTANT: You must set up a Tiingo account for your API keys. 

### Prerequisites
- [Anaconda](https://www.anaconda.com/download/) installed on your system

### Installation
1. **Clone this repository**
   ```bash
   git clone https://github.com/[your-username]/Portfolio-Optimization_Enhanced.git
   cd Portfolio-Optimization_Enhanced
   ```

2. **Create and activate Anaconda environment**
   ```bash
   conda create -n portfolio-opt python=3.9
   conda activate portfolio-opt
   ```

3. **Install required packages**
   ```bash
   conda install -c conda-forge pandas numpy matplotlib seaborn jupyter tqdm
   conda install -c conda-forge tiingo pandas-datareader
   pip install yfinance
   ```

### Configuration
1. **Open the main Python file**
   - Navigate to the main code file in your editor or Jupyter Lab
   - Replace API key placeholders with your actual keys:
     ```python
     # Replace with your Tiingo API key
     config = {'api_key': "YOUR_TIINGO_API_KEY_HERE", 'session': True}
     
     # Replace with your FMP API key
     FMP_API_KEY = "YOUR_FMP_API_KEY_HERE"
     ```

2. **Launch Jupyter Lab**
   ```bash
   jupyter lab
   ```

3. **Run the optimizer**
   - Open the Jupyter notebook
   - Adjust parameters as needed (stocks, iterations, optimization goal)
   - Run all cells to generate portfolio allocation and visualizations

GitHub Wiki coming soon for more detailed instructions.
```
--------------------------------------------------------------------------------------------------------------------------
5. Implementation Note
--------------------------------------------------------------------------------------------------------------------------
This enhancement focuses exclusively on the main optimization module and does not modify other files 
in the original project. All enhancements have been integrated into a single comprehensive Python file 
for simplicity and ease of use.

**Main file for enhanced version:** `enhanced_mpt_optimizer.py`

--------------------------------------------------------------------------------------------------------------------------
6. Acknowledgment
--------------------------------------------------------------------------------------------------------------------------
This project builds upon the excellent Modern Portfolio Theory implementation by Daniel Carpenter. The original work established the foundation for using PSO in portfolio optimization, which we've extended with additional statistical techniques and practical investment features.

--------------------------------------------------------------------------------------------------------------------------
7. License
--------------------------------------------------------------------------------------------------------------------------
This project is licensed under the MIT License, maintaining the same license as the original repository by Daniel Carpenter.

MIT License

Copyright (c) 2022 Daniel Carpenter (original work)
Copyright (c) 2025 AssetMatrix500 (modifications and enhancements)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


--------------------------------------------------------------------------------------------------------------------------
8. Professional Services
--------------------------------------------------------------------------------------------------------------------------

While this code is freely available under the MIT license, I offer professional consulting services for implementation, customization, and strategic advice:

- **Optimal Settings Configuration**: Access to research-backed parameter settings that maximize real-world performance
- **Portfolio Selection**: Suggested portfolios for optimal performance across different risk profiles
- **Strategy Customization**: Optimization parameter tuning for specific investment goals
- **Portfolio Analysis**: Detailed risk/return analysis of existing portfolios
- **Educational Workshops**: Training for teams or individuals on portfolio optimization

**[Hire me on Fiverr](https://www.fiverr.com/s/8zDNb5z)** for professional portfolio optimization services.

--------------------------------------------------------------------------------------------------------------------------
9. Attribution and Contributions
--------------------------------------------------------------------------------------------------------------------------
This repository is a fork of Daniel Carpenter's Portfolio Optimization project 
(https://github.com/Daniel-Carpenter/Portfolio-Optimization), which provided the 
foundational code and structure.

Key enhancements in this fork include:
- Implementation of Bayesian shrinkage techniques with asset-specific priors
- Factor model for covariance matrix with Blume-adjusted betas
- Enhanced data collection from multiple financial APIs
- Comprehensive performance analysis and visualization
- Portfolio simulation and comparison with benchmarks

While this code is freely available under the MIT license, professional implementation,
customization, and consulting services are available. Please contact us for more information.

--------------------------------------------------------------------------------------------------------------------------
10. Disclaimer
--------------------------------------------------------------------------------------------------------------------------
This software is provided for educational and informational purposes only. It is not intended
as financial advice or a recommendation to buy or sell any securities. Investment involves
risk, and past performance is not indicative of future results. Users should conduct their
own research and consult with a qualified financial advisor before making investment decisions.

The authors and contributors to this software assume no responsibility for any losses, damages,
or other liabilities that may arise from the use of this software or the information it provides.