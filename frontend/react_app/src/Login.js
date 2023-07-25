import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/login/', { username, password });
      setMessage('登录成功！');
    } catch (error) {
      setMessage('用户名或密码错误！');
    }
  };

  return (
    <div>
      <h2>登录</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="用户名"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <br />
        <input
          type="password"
          placeholder="密码"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <br />
        <button type="submit">登录</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default Login;