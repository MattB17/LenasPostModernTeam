import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { Login } from './login/login';
import { NewUser } from './new-user/new-user';
import { CamperInfo } from './camper-info/camper-info';
import { CamperSchedule } from './camper-schedule/camper-schedule';
import { CampStats } from './camp-stats/camp-stats';
import { CampEnrollment } from './camp-enrollment/camp-enrollment';

const routes: Routes = [
  {
    path: '',
    component: Login
  },
  {
    path: 'new-user',
    component: NewUser
  },
  {
    path: 'camper-info',
    component: CamperInfo
  },
  {
    path: 'camper-schedule',
    component: CamperSchedule
  },
  {
    path: 'camp-stats',
    component: CampStats
  },
  {
    path: 'camp-enrollment',
    component: CampEnrollment
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
