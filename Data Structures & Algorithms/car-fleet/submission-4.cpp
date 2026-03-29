class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // Subtract from the target the position of each car

        // Time = Distance / Speed
        // Use time to determine the number of car fleets,
        // So when previous car/s takes shorter time then the current car, they are of the same fleet
        int n = position.size();
        vector<pair<int, double>> cars;

        // Store (position, time to reach target)
        for(int i = 0; i < n; i++){
            double time = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }

        // Sort cars by position descending, largest to smallest miles
        sort(cars.begin(), cars.end(),
            [](auto &a, auto &b){
                return a.first > b.first;
            }
        );

        int fleets = 0;
        double maxTime = 0;

        // Process from closest to target
        for(auto &car: cars){
            if(car.second > maxTime){
                fleets++;
                maxTime = car.second;
            }
        }
        return fleets;
    }
};
