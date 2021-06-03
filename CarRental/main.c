#include <stdio.h>
#include <stdlib.h>
#include "conio2.h"
#include "car.h"


int main()
{
          gotoxy(25,10);
          textcolor(YELLOW);
          printf("Welcome To Car Rental System");
          gotoxy(20,13);
          textcolor(LIGHTGREEN);
          printf("*Rent a Car and go wherever you want *");
          _getch();
          textcolor(YELLOW);
          addAdmin();
          User *usr;
          int result;
          int choice,type,i;
          while(1)
          {

               clrscr();
               textcolor(LIGHTGREEN);
               gotoxy(32,2);
               printf(" CAR RENTAL SYSTEM");
               gotoxy(1,8);
               textcolor(YELLOW);
               for(i=0;i<80;i++)
               {

                    printf("*");

               }
               gotoxy(1,17);
               for(i=0;i<80;i++)
               {

                    printf("*");
               }
               gotoxy(32,10);
               textcolor(YELLOW);
                printf("1. Admin");
                gotoxy(32,12);
                printf("2. Employee");
                gotoxy(32,14);
                textcolor(WHITE);
                int k;
                printf(" Select Your Role:");
                do
                {

                    scanf("%d",&type);
                    k=0;
                    if(type==1)
                    {

                         do
                         {

                              usr=getInput();
                              if(usr!=NULL)
                              {

                                    k=checkUserExist(*usr,"admin");
                              }
                              else
                              {

                                     break;
                              }
                         }while(k==0);


                         if(k==1)
                         {

                              gotoxy(30,14);
                              textcolor(LIGHTGREEN);
                              printf("Login Accepeted");
                              gotoxy(1,20);
                              textcolor(WHITE);
                              printf("Press any key to continue");
                              _getch();
                              while(1)
                              {

                                     clrscr();
                                     choice=adminMenu();
                                     if(choice==7)
                                     {

                                           clrscr();
                                           break;

                                     }
                                     switch(choice)
                                     {

                                        case 1:
                                                   clrscr();
                                                   addEmployee();
                                                   break;
                                        case 2:
                                                  clrscr();
                                                  addCarDetails();
                                                 break;


                                        case 3:
                                                 clrscr();
                                                 viewEmployee();
                                                 break;
                                        case 4:
                                                  clrscr();
                                                  showCarDetails();
                                                break;
                                        case 5:
                                                 clrscr();
                                                 result=deleteEmp();
                                                 if(result==0)
                                                 {

                                                      gotoxy(15,14);
                                                      textcolor(LIGHTRED);
                                                      printf("Sorry! No Employee Found With The Given Employee Id");
                                                      textcolor(WHITE);
                                                      printf("\n\nPress Any Key To Go Back To The Main Menu");
                                                      _getch();
                                                 }
                                                 else if(result==1)
                                                 {

                                                      gotoxy(25,14);
                                                      textcolor(LIGHTGREEN);
                                                      printf("Record Deleted Successfully");
                                                      textcolor(WHITE);
                                                      printf("\n\n Press Any Key To Go Back Main Menu");
                                                      _getch();
                                                 }
                                                break;
                                        case 6:
                                                    clrscr();
                                                    result=deleteCarDetails();
                                                    if(result==0)
                                                    {

                                                         gotoxy(15,14);
                                                         textcolor(LIGHTRED);
                                                         printf("Sorry!No car found with the given Employee id");
                                                         textcolor(WHITE);
                                                         printf("\n\nPress any key to go back to the main menu");
                                                         _getch();

                                                    }
                                                    else if(result==1)
                                                    {

                                                             gotoxy(25,14);
                                                             textcolor(LIGHTGREEN);
                                                             printf("Record Delete Successfully");
                                                             textcolor(WHITE);
                                                             printf("\n\nPress any key to go to back to the menu");
                                                             _getch();
                                                    }
                                                 break;

                                        default:
                                                printf("Incorrect choice:");
                                                _getch();

                                     }

                              }

                         }


                   }
                    else if(type==2)
                    {
                        do
                        {

                               usr=getInput();
                               if(usr!=NULL)
                               {

                                    k=checkUserExist(*usr,"emp");

                               }
                               else
                               {

                                    break;

                               }

                        }while(k==0);
                        if(k==1)
                        {

                             gotoxy(30,14);
                             textcolor(LIGHTGREEN);
                             printf("Login Accepetd!");
                             gotoxy(1,20);
                             textcolor(WHITE);
                             printf("Press Any key to continue");
                             _getch();
                             while(1)
                             {

                                  clrscr();
                                  choice=empMenu();
                                  if(choice==5)
                                  {

                                       clrscr();
                                       break;
                                  }
                                  switch(choice)
                                  {

                                      case 1:
                                        clrscr();
                                        int j;
                                        do
                                        {

                                                clrscr();
                                                j=rentcar();
                                                if(j==0)
                                                {

                                                     printf("Booking Cancelled\ntry again");

                                                }
                                                _getch();
                                        }while(j==0);
                                        _getch();
                                        break;
                                    case 2:

                                         clrscr();
                                         bookedCarDetails();
                                         _getch();
                                         break;
                                    case 3:
                                         clrscr();
                                         availableCarDetails();
                                         _getch();
                                         break;
                                    case 4:
                                           clrscr();
                                           showCarDetails();
                                           break;
                                    default:
                                        printf("Wrong choice:");
                                  }
                             }
                        }

                    }
                    else
                    {
                        textcolor(LIGHTRED);
                gotoxy(30,20);
                        printf("Invalid User Type:");
                        _getch();
                        gotoxy(30,20);
                        printf("\t\t\t");
                        gotoxy(50,14);
                        printf("\t");
                        gotoxy(50,14);
                        textcolor(WHITE);
                    }
                }
                while(type!=1&&type!=2);

          }




         return 0;
}
