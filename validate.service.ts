import { Injectable } from '@angular/core';

@Injectable()
export class ValidateService {

  constructor() { }

  validateRegister(user) {
    if (user.name === undefined || user.email === undefined ||
      user.username === undefined || user.password === undefined) {
      return false;
    } else {
      return true;
    }
  }

  validteEmail(email) {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  }
}