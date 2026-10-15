import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  login = '';
  password = '';
  errorMessage = '';

  constructor(private router: Router) {}

  iniciarSesion(): void {
    if (this.login === 'user2335' && this.password === 'pasword') {
      sessionStorage.setItem('isLoggedIn', 'true');
      this.router.navigate(['/catalogos']);
    } else {
      this.errorMessage = 'Usuario o contraseña incorrectos.';
    }
  }
}
