# Django Todo App API

A simple set of API Endpoints Developed Using Djnago REST Framework

## API Reference

#### Get all tasks

```http
  GET /api/tasks
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Returns all tasks stored in DB |

#### create a task
```http
  POST /api/tasks
```


| Parameter      | Type     | Description                        |
| :--------      | :------- | :--------------------------------  |
| `id`           | `integer`| **Required**. Id of item to create |
| `title`        | `string` |  title of item to create           |
| `priority`     | `integer`|  priority of item to create        |
| `is_completed` | `boolean`| status of item to create |
| `dueDate`      | `date-time`| Due date of item to create |

#### Get all incomplete tasks

```http
  GET /api/todo
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Returns all incomplete tasks stored in DB |

#### Mark a task as completed

```http
  PUT /api/done/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `is_completed`      | `boolean` | Status of the task |

#### Delete a Task from DB

```http
  DELETE /api/done/${id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Delets a tasks from DB |