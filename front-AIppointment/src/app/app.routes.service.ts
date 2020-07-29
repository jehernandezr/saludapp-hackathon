import { RouterModule, Route } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import {LandingPageComponent} from './../app/landingpage/landingpage.component';
import { HomeUserComponent } from './pacient/home/homeuser.component';

const routes: Route[] = [
  { path: '', component: LandingPageComponent},
  { path: 'p/home', component: HomeUserComponent},
  { path: '**', redirectTo: ''},

];

export const AppRoutes: ModuleWithProviders = RouterModule.forRoot(routes);
