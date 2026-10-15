import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { CatalogosService } from './catalogos.service';

@Component({
  selector: 'app-catalogos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './catalogos.component.html',
  styleUrls: ['./catalogos.component.css']
})
export class CatalogosComponent implements OnInit {
  estadoCambios: string[] = [];
  periodos: string[] = [];
  errorEstados = '';
  errorPeriodos = '';

  constructor(
    private catalogosService: CatalogosService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.cargarEstadoCambios();
    this.cargarPeriodos();
  }

  cargarEstadoCambios(): void {
    this.catalogosService.getEstadoCambios().subscribe({
      next: (data) => this.estadoCambios = data,
      error: () => this.errorEstados = 'No se pudo cargar el catálogo de estados.'
    });
  }

  cargarPeriodos(): void {
    this.catalogosService.getPeriodos().subscribe({
      next: (data) => this.periodos = data,
      error: () => this.errorPeriodos = 'No se pudo cargar el catálogo de periodos.'
    });
  }

  cerrarSesion(): void {
    sessionStorage.removeItem('isLoggedIn');
    this.router.navigate(['/login']);
  }
}
