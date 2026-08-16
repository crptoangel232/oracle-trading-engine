# Oracle Trading Engine — Autonomous AI Trading Platform

> Multi-strategy AI analysis, real-time risk management, and broker-agnostic execution.

The Oracle Trading Engine is an autonomous AI-powered trading platform built on the Base44 platform. It analyzes market regimes across multiple timeframes, selects optimal strategies, validates every trade through a 15+ parameter risk engine, and executes through a unified broker adapter interface.

## 🎯 Key Features

- **AI Market Analysis** — Multi-timeframe regime detection with confidence scoring
- **10 Trading Strategies** — Trend following, breakout, mean reversion, momentum, S/R, supply/demand, liquidity, volatility, news reaction, multi-timeframe confluence
- **Risk Engine** — 15+ risk parameters including max drawdown, daily/weekly loss limits, exposure caps, and emergency policies
- **Broker Adapter** — Unified interface supporting Forex, Crypto, Stocks, and multi-asset brokers
- **16-Entity Data Model** — Complete trading system architecture from accounts to audit logs
- **3 Trading Modes** — Paper → Signal → Live Autonomous (progressive autonomy)
- **Immutable Audit Logs** — Every decision, order, and system event logged permanently

## 🏗 Architecture

```
Market Data → Oracle Engine → Risk Engine → Broker Adapter → Position
```

### Three Backend Engines

| Engine | Function | Purpose |
|--------|----------|---------|
| Oracle Engine | `oracleEngine` | AI analysis, regime detection, strategy selection, trade decisions |
| Risk Engine | `riskEngine` | Multi-parameter risk validation, position sizing, exposure management |
| Broker Adapter | `brokerAdapter` | Broker API abstraction, order management, position tracking |

## 📊 Trading Modes

1. **Paper Trading** (default) — Full simulation with real market data, no real money
2. **Signal Mode** — AI generates signals, human approves before execution
3. **Live Autonomous** — Full autonomous trading, requires explicit user enable

## 📈 Strategies

| # | Strategy | Category |
|---|----------|----------|
| 1 | Dynamic Trend Rider | Trend Following |
| 2 | Volatility Breakout | Breakout |
| 3 | Band Reversion Pro | Mean Reversion |
| 4 | RSI Momentum Surge | Momentum |
| 5 | Level Sniper | Support/Resistance |
| 6 | Zone Hunter | Supply/Demand |
| 7 | Liquidity Sweep | Liquidity Structure |
| 8 | ATR Squeeze Play | Volatility |
| 9 | News Spike Catcher | News Reaction |
| 10 | Confluence Matrix | Multi-Timeframe |

## 🗃 Data Model (16 Entities)

**Core Trading:** TradingAccount, Order, Position, Trade

**Market Intelligence:** Asset, MarketData, NewsEvent, AIAnalysis

**Strategy Layer:** Strategy, StrategyVersion, TradeDecision, Backtest, ForwardTest

**Risk & Control:** RiskProfile, PerformanceMetric, Alert, AuditLog, SystemEvent, BrokerConnection

## 🛡 Risk Parameters

| Parameter | Default |
|-----------|---------|
| Max Risk Per Trade | 2% |
| Max Daily Loss | 5% |
| Max Weekly Loss | 10% |
| Max Drawdown | 20% |
| Max Open Positions | 5 |
| Max Exposure Per Asset | 15% |
| Max Correlated Exposure | 25% |
| Max Consecutive Losses | 5 |
| Min AI Confidence | 60% |
| Capital Preservation Threshold | 15% |

**Emergency Policy:** At 20% drawdown, the system auto-closes all positions and pauses trading.

## 💱 Supported Assets

| Asset | Class |
|-------|-------|
| BTC/USD | Crypto |
| ETH/USD | Crypto |
| EUR/USD | Forex |
| GBP/USD | Forex |
| USD/JPY | Forex |
| AAPL | Stock |
| TSLA | Stock |
| XAU/USD | Commodity |
| SPX500 | Index |
| SOL | Crypto |

## 🛠 Technology

- **Platform:** Base44 (React + Tailwind + Vite)
- **Backend:** 3 deployed functions (oracleEngine, riskEngine, brokerAdapter)
- **Database:** 16 entities with row-level security and audit logging
- **AI:** Multi-timeframe analysis, regime detection, confidence scoring
- **Brokers:** OANDA, Binance, Interactive Brokers (adapter pattern)
- **Security:** API key abstraction, immutable audit logs, emergency policies

## 📌 Project Info

- **Builder:** Hawanatu Kargbo
- **Contact:** 076988619 · oswokceo@gmail.com
- **Status:** Paper trading mode active

---

*Built for autonomous, intelligent, risk-managed trading.*
