import { Injectable } from "@angular/core";
//import { Http, Headers } from "@angular/http";
import { HttpClient } from '@angular/common/http';
//import "rxjs/add/operator/map";
import { Observable, Subject, map } from 'rxjs';

import { tokenNotExpired } from "angular2-jwt";

@Injectable()
export class AuthenticationService {
  authToken: any;
  user: any;

  constructor(private _http: HttpClient) { }

  registerUser(user) {
    //const headers = new Headers();
    //headers.append("Content-Type", "application/json");
    const headers = {'content-type': 'application/json'}
    return this._http.post("http://localhost:3000/users/register", user,
      { headers: headers })
      /*.subscribe(response=>{
        console.log("POST completed successfully, new user registered"+response);
      },
      error => {
        console.log("POST failed with errors");
      },
      () =>{
        console.log("POST")
      }
      )
      
      //map(res => res.json());*/
  }

  authenticateUser(user) {
    //const headers = new Headers();
    //headers.append("Content-Type", "application/json");
    const headers = {'content-type': 'application/json'}
    return this._http.post("http://localhost:3000/users/authenticate", user,
      { headers: headers })
      
      /*.subscribe(
        response => {
        console.log("POST completed successfully, user authenticated"+response);
      },
      error => {
        console.log("POST failed with errors");
      },
      () =>{
        console.log("POST")
      })
  */
  }

  getProfile() {
    //const headers = new Headers();
    this.loadToken();
    //headers.append("Authorization", this.authToken);
    //headers.append("Content-Type", "application/json");
    const headers = {"Authorization": this.authToken, 'content-type': 'application/json' , }
    return this._http.get("http://localhost:3000/users/profile",
      { headers: headers })
      /*.subscribe(response=>{
        console.log("GET completed successfully, user found "+response);
      },
      error => {
        console.log("GET failed with errors");
      },
      () =>{
        console.log("GET")
      })*/
  }

  storeUserData(data) {
    localStorage.setItem("id_token", data.token);
    localStorage.setItem("user", JSON.stringify(data.user));
    this.authToken = data.token;
    this.user = data.user;
  }

  loadToken() {
    this.authToken = localStorage.getItem("id_token");
  }

  loggedIn() {
    return tokenNotExpired("id_token");
  }

  logout() {
    this.authToken = null;
    this.user = null;
    localStorage.clear();
  }
}