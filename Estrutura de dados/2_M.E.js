class TaskManager {
    constructor() {
      this.tasks = [];
      this.nextId = 1;
    }
  
    addTask(title, description, status = 'pendente', tags = []) {
      const newTask = {
        id: this.nextId++,
        title,
        description,
        status,
        tags: new Set(tags),
      };
      this.tasks.push(newTask);
      return newTask;
    }
  
    updateTask(id, updates) {
      const task = this.tasks.find(task => task.id === id);
      if (!task) return null;
      Object.assign(task, updates);
      return task;
    }
  
    removeTask(id) {
      const taskIndex = this.tasks.findIndex(task => task.id === id);
      if (taskIndex === -1) return null;
      return this.tasks.splice(taskIndex, 1)[0];
    }
  
    filterTasksByStatus(status) {
      return this.tasks.filter(task => task.status === status);
    }
  
    addTagToTask(id, tag) {
      const task = this.tasks.find(task => task.id === id);
      if (!task) return null;
      task.tags.add(tag);
      return task;
    }
  
    removeTagFromTask(id, tag) {
      const task = this.tasks.find(task => task.id === id);
      if (!task) return null;
      task.tags.delete(tag);
      return task;
    }
  
    listAllTags() {
      const tagsMap = {};
      this.tasks.forEach(task => {
        task.tags.forEach(tag => {
          if (!tagsMap[tag]) tagsMap[tag] = [];
          tagsMap[tag].push(task);
        });
      });
      return tagsMap;
    }
}
  

const manager = new TaskManager();
manager.addTask("Task 1", "Description 1", "pendente", ["urgent", "work"]);
manager.addTask("Task 2", "Description 2", "em progresso", ["work"]);
manager.updateTask(1, { status: "concluída" });
manager.addTagToTask(2, "important");
manager.removeTagFromTask(2, "work");
console.log(manager.filterTasksByStatus("concluída"));
console.log(manager.listAllTags());