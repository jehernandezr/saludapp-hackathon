import { RouterModule, Route } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import {LandingPageComponent} from './../app/landingpage/landingpage.component';
import { HomeUserComponent } from './pacient/home/homeuser.component';
import { HomeDoctorComponent } from './doctor/home/homedoctor.component';
import { AgendaDoctorComponent } from './doctor/agenda/agendadoctor.component';

const routes: Route[] = [
  { path: '', component: LandingPageComponent},
  { path: 'p/home', component: HomeUserComponent},
  { path: 'd/home', component: HomeDoctorComponent},
  { path: 'd/agenda', component: AgendaDoctorComponent},
  { path: '**', redirectTo: ''},

];

export const AppRoutes: ModuleWithProviders = RouterModule.forRoot(routes);
