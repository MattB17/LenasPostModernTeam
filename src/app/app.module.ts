import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Login } from './login/login';
import { NewUser } from './new-user/new-user';
import { CamperInfo } from './camper-info/camper-info';
import { CamperSchedule } from './camper-schedule/camper-schedule';
import { CampStats } from './camp-stats/camp-stats';
import { CampEnrollment } from './camp-enrollment/camp-enrollment';

@NgModule({
  declarations: [
    AppComponent,
    Login,
    NewUser,
    CamperInfo,
    CamperSchedule,
    CampStats,
    CampEnrollment,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
