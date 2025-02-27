#include <iostream>
using namespace std;

int main(){
    int num1,num2;
    cin >> num1;
    cin >> num2;
    
    if (num1 > 0){
        if (num2 > 0){
            cout << 1 << endl;
        } else {
            cout << 4 << endl;
        }
    } else {
        if (num2 < 0){
            cout << 3 << endl;
        } else {
            cout << 2 << endl;
        }
    }
    return 0;
}