/*
We need to build a mathematical model for the problem first. The following is the description of the model.
Assume at each intersection, there is a probability parameter that a new customer will show up. Moreover,
at each time step, at each intersection, for existing waiting customers, there is a probability parameter 
the existing customer will cancel the order.

We assume the destination a customer is evenly distributed in the rest of the intersections.

The business objective is to get as many customers as possible at unit time, meanwhile minimize the total
traveling distance for those customers who take our car. 

We here implement a heuristic algorithm to achieve this business objective:


 *
 *
 *
 *
 */

#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <set>
#include <map>

using namespace std;

int N; // size of the grid
double new_prob = 0.1;
double cancel_prob = 0.0;
int total_time = 100;
double customer_param = 0.5;
double distance_param = -1 + customer_param;
int total_customers_in_car;
int total_distance = 0;
int customers = 0;


//This function calculate the value of positions by adding reciprocal of distances
//from current position to waiting customers and the destinations of in car customers
//
double  get_value(const multiset<pair<int,int>>& customers_in_car,
	              const multimap<pair<int,int>,
				  pair<int,int>>& customers_waiting,
	              int i,
				  int j) {
	double s = 0;
	for(auto it= customers_in_car.begin(); it!= customers_in_car.end(); it++){
		s += 1/(0.0001+distance_param*abs(it->first - i) + abs(it->second - j));
	}
	for(auto it = customers_waiting.begin(); it != customers_waiting.end(); it++){
		s += 1/(0.0001+customer_param*abs(it->first.first - i)+ abs(it->first.second - j));
	}
	return s;

}

// This is simplly finding the nearest intersection from current intersection to
// waiting customers and the destinations of in car customers.
pair<int,int> get_nearest(const multiset<pair<int,int>>& customers_in_car,
	             const multimap<pair<int,int>,pair<int,int>>& customers_waiting,
	             int i, int j) {
	int x, y;
	int v = 4*N;
	for(auto it= customers_in_car.begin(); it!= customers_in_car.end(); it++) {
	    auto d = distance_param*abs(it->first - i) + abs(it->second - j);
		if(d<v){
		    v = d;
			x = it->first;
			y = it->second;
		}
	}
	for(auto it = customers_waiting.begin(); it != customers_waiting.end(); it++){
	    auto d = customer_param*abs(it->first.first - i)+ abs(it->first.second - j);
		if(d<v){
		    v = d;
			x = it->first.first;
			y = it->first.second;
		
		}

	}
	return pair<int,int>(x,y);

}

int total_customers = 0;



int main(int argc, char** argv) {
	std::stringstream str(argv[1]);
    str>> N;

    // Use a multimap to record customers at an intersection, with values as destinations.
    multimap<pair<int, int>, pair<int, int> > customers_waiting;
	multiset<pair<int,int>> customers_in_car; 
    
    // initial point of the car
	int i = N/2, j = N/2;
	int current_destination_x, current_destination_y;
    
    for(int t = 0; t < total_time; t++){
		    cout<<"\n At time stamp "<<t<< ""<<'\n';
			//customers get off the car
	        for(auto it = customers_in_car.begin(); it != customers_in_car.end();){
				if (it->first == i and it->second == j)
					it = customers_in_car.erase(it);
				else
					it++;
			}	    
            // customers get on the car
			for(auto it = customers_waiting.lower_bound(pair<int, int>(i,j)); it != customers_waiting.upper_bound(pair<int,int>(i,j));){
				customers_in_car.insert(it->second);
                it = customers_waiting.erase(it);

				customers++;
			}
            
            
            // choose the greedy next intersection to go
            
			map<pair<int,int>, double> add_value;
			for(int k = -1;k<2;k++)
				for(int p=-1;p<2; p++){
					if((k!=0 or p!=0) and (k==0 or p==0))
						if ( i+k>=0 and i+k<N and j+p >=0 and j+p<N){
							add_value[pair<int,int>(k,p)] = get_value(customers_in_car, customers_waiting, i+k,j+p) ;
						}
				}

			int k = 0, p = 0;
			double value = add_value[pair<int,int>(0,0)];
			for (auto it = add_value.begin();it!= add_value.end(); it++){
				if (it->second > value){
				    k = it->first.first;
					p = it->first.second;
					value = it->second;
					cout<<value<<" "<<value<<'\n';
				}
			
			}
			
			
			if (k==0 and p==0){
				while(true){
					k = rand() % 2;
					p = rand() % 2;
					if (k==0)
						k = -1;
					if(p==0)
						p = -1;
				    if(i+k>=0 and i+k<N and j+p>=0 and j+p<N){
					
					    i += k;
						j += p;
						break;
					
					}
				}
			}

			auto des = get_nearest(customers_in_car, customers_waiting, i, j);
			auto prev_x = i, prev_y=j;
			/*
			if(des.first>i)
				i++;
			if(des.first < i)
				i--;

            if(des.second>j)
				j++;
			if(des.second<j)
				j--;
			*/
			i += k;
			j += p;
			total_customers_in_car = customers_in_car.size();
			//if (k!=0 or p!=0)
             //   total_distance += total_customers_in_car;
            total_distance += total_customers_in_car*(abs(i-prev_x)+ abs(j-prev_y));
            cout<<"Current position "<<i<<" "<<j<<'\n';
            cout<<"Number of customers in car "<< total_customers_in_car<<'\n';
			// updates of customers at all intersections
			
				//customer could cancel the order with respect to probability 
			
				for (auto it=customers_waiting.begin(); it!=customers_waiting.end(); ){
				    double r = ((double) rand() / (RAND_MAX));
					if (r<= cancel_prob ){
						it = customers_waiting.erase(it);
						total_customers--;
					}
				    else
						it++;
				}
                double r;
				int count = 0;
				while(count< N*N/2){
				    r = ((double) rand() / (RAND_MAX));

				    if (r< new_prob){
				        auto x1 = rand() % N;
					    auto y1 = rand() % N;
					    auto x2 = rand() % N;
					    auto y2 = rand() % N;

                   // if (total_customers< N*N/2){
					customers_waiting.insert(pair<pair<int,int>, pair<int, int>>(pair<int,int>(x1,y1), pair<int, int>(x2,y2)));
					total_customers++;
					//cout<<"customers waiting"<<customers_waiting.size()<<'\n';
					    //cout<<"new customers at "<<i<<" "<<j<<"to destination "<<x<< " "<<y<<'\n';
				
				    }
                    count++;
				}
	
	
	}
	cout<<"\n";
	cout<<"Summery:"<<'\n';
	cout<<"Total time stamps: "<< total_time <<'\n';
	cout<<"Scale of the map: "<<N<<"x"<<N<<'\n';
    cout<<"Total distance*customers: "<<total_distance<<'\n';
    cout<<"Total customers that have been waiting: "<<total_customers<<'\n';
    cout<<"Total customers who have entered the car "<< customers<<'\n';

}
