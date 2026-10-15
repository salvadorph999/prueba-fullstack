import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { CatalogosComponent } from './catalogos/catalogos.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'catalogos', component: CatalogosComponent, canActivate: [authGuard] },
];
