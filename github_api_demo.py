#!/usr/bin/env python3
"""
GitHub API Demo Script

This script demonstrates how to use GitHub API tools.
"""

import requests

def search_repositories(query, per_page=10):
    """
    Search for repositories on GitHub.
    
    Args:
        query (str): Search query
        per_page (int): Number of results to return
        
    Returns:
        dict: JSON response from GitHub API
    """
    url = "https://api.github.com/search/repositories"
    params = {
        'q': query,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    return response.json()

def get_repository_info(owner, repo):
    """
    Get information about a specific repository.
    
    Args:
        owner (str): Repository owner
        repo (str): Repository name
        
    Returns:
        dict: JSON response from GitHub API
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    return response.json()

def main():
    """
    Main function to demonstrate GitHub API usage.
    """
    print("GitHub API Demo")
    print("=" * 20)
    
    # Search for repositories
    print("\nSearching for 'python flask chatbot' repositories...")
    result = search_repositories("python flask chatbot", 5)
    print(f"Found {result['total_count']} repositories")
    
    # Display first few results
    for i, repo in enumerate(result['items'][:3]):
        print(f"\n{i+1}. {repo['full_name']}")
        print(f"   Description: {repo['description']}")
        print(f"   Stars: {repo['stargazers_count']}")
        print(f"   URL: {repo['html_url']}")

if __name__ == "__main__":
    main()