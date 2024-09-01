def select(columns: str, table: str, conditions: str, offset: str = "NULL", limit: str = "NULL") -> str:
	"""SELECT"""
	return f"SELECT {columns} FROM {table} WHERE {conditions} OFFSET {offset} LIMIT {limit};"


def insert(table: str, columns: str, values: str) -> str:
	"""INSERT"""
	return f"INSERT INTO {table} ({columns}) VALUES ({values});"


def update(table: str, column: str, value: str, conditions: str) -> str:
	"""UPDATE"""
	return f"UPDATE {table} SET {column} = {value} WHERE {conditions};"


def multiple_update(table: str, columns: str, values: str, conditions: str) -> str:
	"""MULTIPLE UPDATE"""
	columns_values = ", ".join(f"{column} = {value}" for column, value in zip(columns.split(","), values.split(",")))
	return f"UPDATE {table} SET {columns_values} WHERE {conditions};"


def delete(table: str, conditions: str) -> str:
	"""DELETE"""
	return f"DELETE FROM {table} WHERE {conditions};"
