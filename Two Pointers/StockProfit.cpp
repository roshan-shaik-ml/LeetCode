/**
 * LeetCode [121]: Best Time to Buy and Sell Stock
 * 
 * Say you have an array prices for which the ith element is the price of a given stock on day i.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 * 
 * Approach:
 * Initialize two pointers, leadingEdge and trailingEdge, to iterate through the prices array.
 * Iterate through the array, updating trailingEdge when the price decreases and profit when the price increases.
 * Return the maximum profit obtained.
 * 
 * Code with Comments:
 */

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Disabling synchronization with C standard streams for faster I/O
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        
        // If there are less than two prices, no profit can be made
        if(prices.size() < 2)
            return 0;

        // Initialize pointers and profit
        int leadingEdge = 1; // Pointer to the current day
        int trailingEdge = 0; // Pointer to the day to buy stock
        int profit = 0; // Maximum profit so far

        // Iterate through the prices array
        while(leadingEdge < prices.size()) {
            int sold = prices[leadingEdge]; // Price of the stock on the current day
            int bought = prices[trailingEdge]; // Price of the stock on the day it was bought
            // If the current price is less than the buying price, update the buying day
            if(sold < bought) {
                trailingEdge = leadingEdge;
            } 
            // If the current price is greater than the buying price, calculate profit
            else if(sold > bought) {
                profit = max(profit, sold - bought);
            }
            leadingEdge++; // Move to the next day
        }
        return profit; // Return the maximum profit
    }
};
