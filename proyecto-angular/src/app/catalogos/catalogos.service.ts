import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// *** IMPORTANTE: Cambia esta URL según el API que estés usando ***
// Spring Boot (Java):  http://localhost:8080
// FastAPI (Python):    http://localhost:8000
const API_URL = 'http://localhost:8000';

export interface ConceptoCatalogo {
  clave: string;
  descripcion: string;
}

@Injectable({
  providedIn: 'root'
})
export class CatalogosService {

  constructor(private http: HttpClient) {}

  getEstadoCambios(): Observable<string[]> {
    return this.http.get<string[]>(`${API_URL}/estadoCambios`);
  }

  getPeriodos(): Observable<string[]> {
    return this.http.get<string[]>(`${API_URL}/periodos`);
  }

  /** Reporte R13 A-1311: Estado de cambios en el capital contable de la sociedad controladora. */
  getEstadoCambiosCapitalContable(): Observable<ConceptoCatalogo[]> {
    return this.http.get<ConceptoCatalogo[]>(`${API_URL}/estadoCambiosCapitalContable`);
  }
}
