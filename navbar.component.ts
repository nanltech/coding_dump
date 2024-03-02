import { Component, OnInit } from '@angular/core';
import { Router } from "@angular/router";

import { FlashMessagesService } from "angular2-flash-messages";

import { AuthenticationService } from "../../services/auth.service";

@Component({
  selector: 'navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  constructor(
    public _authenticationService: AuthenticationService,
    private _router: Router,
    private _flashMessages: FlashMessagesService) { }

  ngOnInit() {
  }

  onLogoutClick() {
    this._authenticationService.logout();
    this._flashMessages.show("You are logged out", {
      cssClass: "alert-success",
      timeout: 3000
    });
    this._router.navigate(["/login"]);
    return false;
  }
}