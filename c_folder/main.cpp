
#include <iostream>
#include <math.h>
using namespace std;


class Block{
public:
    int x;
    int w;
    int v;
    int m;

    Block(int x,int w,int v,int m){
        this->x=x;
        this->v = v;
        this->m = m;
    };

    bool collide(Block block){
        return not(this->x + this->w < block.x) or (this->x > (block.x + block.w));
    };

    int bounce(Block block){
        int sum_M = this->m + block.m;
        int new_V = (this->m-block.m)/sum_M* this->v;
        new_V+= (2*block.m/sum_M)*block.v;
        return new_V;
    };

    bool hit_wall(){
        if (this->x <=0){
            return true;
        };
        return false;
    };

    void reverse(){
        this->v*=-1;
    };

    void update(){
        this->x+=this->v;
    };


};


int main() {
    long v1,v2 = 0;
    long long counter = 0;
    const int DIGITS = 2;
    const long M2 = 10;
    Block block1 = Block(200,20,0,1);
    Block block2 = Block(500,150,-1,M2);
    while (true){
        if (block1.collide(block2)){
            v1 = block1.bounce(block2);
            v2=block2.bounce(block1);
            block1.v=v1;
            block2.v=v2;
            counter= counter+1;

        }
        if (block1.hit_wall()){
            block1.reverse();
            counter= counter+1;
        }

        block1.update();
        block2.update();

        cout << counter << endl;
    }

};