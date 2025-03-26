import React, { useEffect, useState } from 'react';
import AddTaskForm from './AddTaskForm';
import api from '../api';

interface Task {
  name: string,
  done: boolean
}

const TaskList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);

  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks');
      setTasks(response.data);
      console.log('got tasks: ', response.data)
    } catch (error) {
      console.error("Error fetching tasks", error);
    }
  };

  const addTask = async (taskName: string) => {
    try {
      await api.post('/tasks', { name: taskName, done: false });
      fetchTasks();  // Refresh the list after adding a task
    } catch (error) {
      console.error("Error adding task", error);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h2>Tasks List</h2>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task.name}</li>
        ))}
      </ul>
      <AddTaskForm addTask={addTask} />
    </div>
  );
};

export default TaskList;