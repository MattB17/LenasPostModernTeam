import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { Login } from './login/login';
import { NewUser } from './new-user/new-user';
import { CamperInfo } from './camper-info/camper-info';
import { CamperSchedule } from './camper-schedule/camper-schedule';

@NgModule({
  declarations: [
    AppComponent,
    Login,
    NewUser,
    CamperInfo,
    CamperSchedule
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
