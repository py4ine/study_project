// 초기 세팅
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2/promise');
const path = require('path');

const app = express();
const port = 3000;

// 미들웨어 설정
app.use(express.static(path.join(__dirname, 'public')));  // 정적파일 공유 경로 설정
app.use(bodyParser.json());  // Body-parser
app.use(bodyParser.urlencoded({ extended: true }));  // Body-parser

// MySQL 커넥션 풀 설정
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'root1234',
    database: 'mydb'
});

// 파일 서빙
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// user 정보 등록 API
app.post('/users', async (req, res) => {
    const { user_id_email, user_passwd, user_name, user_birth_date, user_sex, user_permission,
        user_bank_num, user_capital, user_loan, user_installment_saving, user_deposit
     } = req.body;
    
    // 필수 필드 확인
    if (!user_id_email || !user_passwd || !user_name || !user_birth_date || user_sex === undefined) {
        return res.status(400).json({ message: 'Missing required fields' });
    }
    
    try {
        const connection = await pool.getConnection();
        const query = 'INSERT INTO tb_user (user_id_email, user_passwd, user_name, \
            user_birth_date, user_sex, user_permission, user_bank_num, user_capital, \
            user_loan, user_installment_saving, user_deposit) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)';
        
        const [result] = await connection.execute(query, [user_id_email, user_passwd, user_name, user_birth_date, user_sex, user_permission,
            user_bank_num, user_capital, user_loan, user_installment_saving, user_deposit]);
        
        connection.relrease();  // 연결반환. 풀로 되돌리기

        res.status(200).json({ message: 'User registered successfully!', id: result.insertId });
    } catch (err) {
        console.error('쿼리 실행 에러:', err);
        res.status(500).send('서버 에러');
    }
    
});


// 서버 시작
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});