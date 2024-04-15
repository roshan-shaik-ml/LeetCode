/*
LeetCode [2391]: Garbage Collection Time Calculation

You are given a list of houses with different types of garbage (paper, glass, metal) at each house and a list of travel times between the houses. You need to calculate the total time required for garbage collection in all houses.

Approach:
1. Calculate the prefix sum of travel times to each house.
2. Iterate through the list of houses and for each house:
    a. Calculate the frequency of each type of garbage.
    b. Update the total time for each type of garbage based on the frequency and travel time.
3. Return the total time required for garbage collection.

Code with Comments:
*/

#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution {
public:
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        // Initialize variables to store total time for each type of garbage
        int paper_time = 0, glass_time = 0, metal_time = 0;
        // Initialize pointers for tracking the last occurrence of each type of garbage
        int glass_ptr = 0, paper_ptr = 0, metal_ptr = 0;
        // Initialize prefix sum of travel times
        vector<int> prefix_travel;
        int curr_sum = 0;
        prefix_travel.push_back(0);

        // Calculate prefix sum of travel times
        for (int i = 0; i < travel.size(); i++) {
            curr_sum += travel[i];
            prefix_travel.push_back(curr_sum);
        }

        // Iterate through the list of houses
        for (int i = 0; i < garbage.size(); i++) {
            string house = garbage[i];
            map<char, int> freq;

            // Calculate frequency of each type of garbage in the current house
            for (auto ch : house) {
                if (freq.find(ch) != freq.end()) 
                    freq[ch]++;
                else
                    freq[ch] = 1;
            }   

            // Update total time for metal garbage
            if (freq.find('M') != freq.end()) {
                int travel_time = prefix_travel[i] - prefix_travel[metal_ptr];
                metal_time += freq['M'] + travel_time;
                metal_ptr = i;
            }
            // Update total time for paper garbage
            if (freq.find('P') != freq.end()) {
                int travel_time = prefix_travel[i] - prefix_travel[paper_ptr];
                paper_time += freq['P'] + travel_time;
                paper_ptr = i;
            }
            // Update total time for glass garbage
            if (freq.find('G') != freq.end()) {
                int travel_time = prefix_travel[i] - prefix_travel[glass_ptr];
                glass_time += freq['G'] + travel_time;
                glass_ptr = i;
            }
        }

        // Calculate total time required for garbage collection
        int total_time = glass_time + paper_time + metal_time;
        return total_time;
    }
};
