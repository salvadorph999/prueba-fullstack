import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// *** IMPORTANTE: Cambia esta URL según el API que estés usando ***
// Spring Boot (Java):  http://localhost:8080
// FastAPI (Python):    http://localhost:8000
const API_URL = 'http://localhost:8000';

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
}
