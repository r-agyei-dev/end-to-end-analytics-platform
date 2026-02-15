# src/dashboard.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def update_dashboard(
    df: pd.DataFrame,
    genre: str = None,
    min_rating: float = 0.0
) -> None:
    """
    Updates dashboard visualizations based on selected genre
    and minimum rating threshold.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned movie dataset.
    genre : str, optional
        Genre to filter by (default is None = all genres).
    min_rating : float, optional
        Minimum vote_average threshold.
    """

    # Defensive copy
    filtered = df.copy()

    # Apply rating filter
    filtered = filtered[filtered["vote_average"] >= min_rating]

    # Apply genre filter (if provided)
    if genre and "genre" in filtered.columns:
        filtered = filtered[
            filtered["genre"].str.contains(genre, case=False, na=False)
        ]

    # If no data remains after filtering
    if filtered.empty:
        print("No data available for selected filters.")
        return

    # ---- Dashboard Layout ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1️⃣ Budget Distribution
    axes[0, 0].hist(filtered["budget"], bins=30)
    axes[0, 0].set_title("Budget Distribution")
    axes[0, 0].set_xlabel("Budget")
    axes[0, 0].set_ylabel("Count")

    # 2️⃣ Revenue Distribution
    axes[0, 1].hist(filtered["revenue"], bins=30)
    axes[0, 1].set_title("Revenue Distribution")
    axes[0, 1].set_xlabel("Revenue")
    axes[0, 1].set_ylabel("Count")

    # 3️⃣ Budget vs Revenue Scatter
    axes[1, 0].scatter(filtered["budget"], filtered["revenue"])
    axes[1, 0].set_title("Budget vs Revenue")
    axes[1, 0].set_xlabel("Budget")
    axes[1, 0].set_ylabel("Revenue")

    # 4️⃣ Average Revenue by Year
    if "release_date" in filtered.columns:
        yearly_avg = (
            filtered.groupby(filtered["release_date"].dt.year)["revenue"]
            .mean()
        )
        axes[1, 1].plot(yearly_avg.index, yearly_avg.values)
        axes[1, 1].set_title("Average Revenue by Year")
        axes[1, 1].set_xlabel("Year")
        axes[1, 1].set_ylabel("Average Revenue")
    else:
        axes[1, 1].text(0.5, 0.5, "No release_date column",
                        horizontalalignment="center")

    plt.tight_layout()
    plt.show()

