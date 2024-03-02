import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { Observable } from 'rxjs';

import { AuthenticationService } from "../../services/auth.service";

@Component({
  selector: "profile",
  templateUrl: "./profile.component.html",
  styleUrls: ["./profile.component.scss"]
})
export class ProfileComponent implements OnInit {
  user: Object;

  constructor(
    private _authenticationService: AuthenticationService,
    private _router: Router) { }

  ngOnInit() {
    this._authenticationService.getProfile().subscribe(
      profile => this.user = profile.user,
      err => {
        console.log(err);
        return false;
      }
    );
  }
}