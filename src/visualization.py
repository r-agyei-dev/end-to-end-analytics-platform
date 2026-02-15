# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_budget_distribution(df):
    df['budget'].hist(bins=30)
    plt.title('Distribution of Movie Budgets')
    plt.show()


def plot_revenue_distribution(df):
    df['revenue'].hist(bins=30)
    plt.title('Distribution of Revenue')
    plt.show()


def plot_budget_vs_revenue(df):
    df.plot(kind='scatter', x='budget', y='revenue')
    plt.title('Budget vs Revenue')
    plt.show()


def plot_correlation_matrix(df):
    corr = df[['budget','revenue','profit','vote_average','runtime']].corr()
    sns.heatmap(corr, annot=True)
    plt.title('Correlation Matrix')
    plt.show()


def plot_yearly_trends(df):
    yearly_trends = df.groupby(df['release_date'].dt.year)[['revenue','budget','profit']].mean()
    yearly_trends.plot(figsize=(10,6))
    plt.title('Average Financial Metrics Over Time')
    plt.show()

