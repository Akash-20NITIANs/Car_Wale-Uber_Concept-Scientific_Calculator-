#ifndef CAR_H_INCLUDED
#define CAR_H_INCLUDED
#include<time.h>

 struct User
{

     char userid[50];
     char pwd[50];
     char name[50];
};

  struct Car
{

    int car_id;
    char car_name[50];
    int capacity;
    int car_count;
    int price;
};

struct Customer_Car_details
{
     int car_id;
     char cust_name[30];
     char pick[30];
     char drop[30];
     struct tm sd,ed;
};

 typedef struct User User;
 typedef struct Car Car;
 typedef struct Customer_Car_details Customer_Car_details;


   void addAdmin();
   User* getInput();
   int checkUserExist(User,char*);
   int adminMenu();
   void addEmployee();
   void viewEmployee();
   void addCarDetails();
   void showCarDetails();
   int deleteEmp();
   int delteCarModel();
   void sub_str(char *,char *,char);
   int empMenu();
   int rentCar();
   int selectCarModel();
   void updateCarCount(int);
   void bookedCarDetails();
   char * getCarName(int);
   int isValidDate(struct tm);
   void availCarDetails();
   void showCarDetails();



#endif // CAR_H_INCLUDED
