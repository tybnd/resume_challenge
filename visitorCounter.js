const AWS = require('aws-sdk');

// Configure AWS SDK with your region
AWS.config.update({ region: 'us-east-1' });

// Create DynamoDB service object
const dynamodb = new AWS.DynamoDB.DocumentClient();

// DynamoDB table name
const tableName = 'cloud-resume-challenge';

// Function to get the current visitor count
const getVisitorCount = async () => {
  const params = {
    TableName: tableName,
    Key: {
      ID: '123' // Use the correct ID from your table
    }
  };

  try {
    const data = await dynamodb.get(params).promise();
    return data.Item ? data.Item.VisitorCount : 0; // Adjust attribute name to 'VisitorCount'
  } catch (err) {
    console.error('Error getting visitor count:', err);
    return 0;
  }
};

// Function to increment the visitor count
const incrementVisitorCount = async () => {
  const currentCount = await getVisitorCount();
  const newCount = currentCount + 1;

  const params = {
    TableName: tableName,
    Item: {
      ID: '123', // Use the correct ID from your table
      VisitorCount: newCount // Adjust attribute name to 'VisitorCount'
    }
  };

  try {
    await dynamodb.put(params).promise();
    console.log('Visitor count updated to:', newCount);
    return newCount;
  } catch (err) {
    console.error('Error updating visitor count:', err);
    return currentCount;
  }
};

// Example usage: Increment and display the visitor count
(async () => {
  const count = await incrementVisitorCount();
  document.getElementById('visitor-count').textContent = count;
})();
