#include <iostream>
using namespace std;

int main(){
    int h, m;
    cin >> h >> m;
    
    if (m - 45 >= 0) {
        cout << h << " " << m - 45 << endl;
    } 
    else {
        if (h == 0) {
            cout << 23 << " " << m + 15 << endl;
        } 
        else {
            cout << h - 1 << " " << m + 15 << endl;
        }
    }

    return 0;
}