import React, { useState, ChangeEvent, FormEvent } from 'react';

interface AddTaskFormProps {
  addTask: (taskName: string) => void;
}

const AddTaskForm: React.FC<AddTaskFormProps> = ({ addTask }) => {
  const [taskName, setTaskName] = useState<string>('');

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (taskName) {
      addTask(taskName);
      setTaskName('');
    }
  };

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTaskName(event.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={taskName}
        onChange={handleChange}
        placeholder="Enter task name"
      />
      <button type="submit">Add Task</button>
    </form>
  );
};

export default AddTaskForm;