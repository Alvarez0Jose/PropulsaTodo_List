import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'TODO List';
  tasks: any = [];
  newTaskTitle = '';

  constructor(private http: HttpClient) {
    this.refreshTasks();
  }

  refreshTasks() {
    this.http.get('http://localhost:8000/tasks/').subscribe((data) => {
      this.tasks = data;
    });
  }

  addTask() {
    // Add this method
    this.http
      .post('http://localhost:8000/tasks/', {
        title: this.newTaskTitle,
        completed: false,
      })
      .subscribe((data) => {
        this.refreshTasks();
      });
  }

  toggleTaskCompletion(task: any) {
    // Explicitly declare task as any
    this.http
      .post(`http://localhost:8000/tasks/${task.id}/set_completed/`, {
        completed: !task.completed,
      })
      .subscribe((data) => {
        this.refreshTasks();
      });
  }
}
