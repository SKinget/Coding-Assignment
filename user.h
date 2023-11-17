#pragma once
using namespace std;

class User
{
private:
string databaseName;
string tableName;
bool loggedIn;
string userID;

public:
User() : dataBaseName(/*not sure about this one yet*/), tableName(/*not sure about this one yet*/), loggedIn(false), userID() {}
User(string databaseName, string tableName);
bool login();
bool logout();
void viewAccountInformation();
void createAccount();
bool getLoggedIn();
string getUserId();
    
}