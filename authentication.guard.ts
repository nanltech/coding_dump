import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { Observable } from 'rxjs';

import { AuthenticationService } from "../services/auth.service";

@Injectable()
export class AuthenticationGuard implements CanActivate {
  constructor(
    private _authenticationService: AuthenticationService,
    private _router: Router) {}

  canActivate() {
    if (this._authenticationService.loggedIn()) {
      return true;
    } else {
      this._router.navigate(["/login"]);
      return false;
    }
  }
}
