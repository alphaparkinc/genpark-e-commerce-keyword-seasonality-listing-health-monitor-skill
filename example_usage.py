from client import ECommerceKeywordSeasonalityListingHealthMonitorClient

def main():
    client = ECommerceKeywordSeasonalityListingHealthMonitorClient()
    res = client.monitor_health_and_seasonality(["fast charger", "travel adapter"], "https://example.com/item")
    print(f"Seasonality Trend: {res['seasonality_trend']}")
    print(f"Keyword Opportunity Score: {res['keyword_opportunity_score']}")

if __name__ == "__main__":
    main()
